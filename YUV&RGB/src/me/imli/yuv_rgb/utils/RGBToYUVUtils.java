package me.imli.yuv_rgb.utils;

import me.imli.yuv_rgb.ben.YUV;

public class RGBToYUVUtils {

	/**
	 * RGB 转 YUV
	 * @param r
	 * @param g
	 * @param b
	 * @return
	 */
	public static boolean RGB2YUV(YUV yuv, byte r, byte g, byte b) {
		int iR = r & 0xff;
		int iG = g & 0xff;
		int iB = b & 0xff;
		return RGB2YUV(yuv, iR, iG, iB);
	}
	
	/**
	 * RGB 转 YUV
	 * @param r int RGB
	 * @param g
	 * @param b
	 * @return
	 */
	public static boolean RGB2YUV(YUV yuv, int r, int g, int b) {
		yuv.y = (int) (0.299 * r + 0.587 * g + 0.114 * b);
		yuv.u = (int) (-0.1687 * r - 0.3313 * g + 0.5 * b) + 128;
		yuv.v = (int) (0.5 * r -0.4187 * g - 0.813 * b) + 128;
		
		if (!yuvAdjust(yuv)) {
			return false;
		}
		
		return true;
	}
	
	
	/**
	 * 对 YUV 出界进行调整
	 * @param yuv
	 */
	public static boolean yuvAdjust(YUV yuv) {
		return true;
	}
	
}
