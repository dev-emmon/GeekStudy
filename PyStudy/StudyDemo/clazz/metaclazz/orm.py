#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/5/12

"""
ORM 框架
"""


class Filed(object):
    def __init__(self, name, column_type):
        self.name = name;
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Filed):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100')


class IntegerField(Filed):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Filed):
                print 'Found mapping: %s ==> %s' % (k, v)
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        # 假设表名和类名一致
        attrs['__table__'] = name
        # 保存属性和列的映射关系
        attrs['__mappings__'] = mappings
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'"Model" object has a no attribute "%s"' % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print 'SQL: %s' % sql
        print 'ARGS: %s' % str(args)


class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


if __name__ == '__main__':
    # 创建一个实例
    u = User(id='1000', name='ZFei', email='zf@imli.me', password='my-pw')
    # 保存到数据库
    u.save()

