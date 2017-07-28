package me.imli.yuv_rgb.utils;

import me.imli.yuv_rgb.ben.RGB;

public class YUVToRGBUtils {

	
	/**
	 * YUV 转 RGB
	 * @param y
	 * @param u
	 * @param v
	 * @return
	 */
	public static boolean YUV2RGB(RGB rgb, byte y, byte u, byte v) {

		// 转成 int 
		int iY = y & 0xff;
		int iU = u & 0xff;
		int iV = v & 0xff;
		
		return YUV2RGB(rgb, iY, iU, iV);
	}
	
	/**
	 * YUV 转 RGB
	 * @param y
	 * @param u
	 * @param v
	 * @return
	 */
	public static boolean YUV2RGB(RGB rgb, int y, int u, int v) {
		
		rgb.r = (int) (y + 1.402 * (v - 128));
		rgb.g = (int) (y - 0.34414 * (u - 128) - 0.71414 * (v - 128));
		rgb.r = (int) (y + 1.772 * (u - 128));
		
		// 调整出界
		if (!rgbAdjust(rgb)) {
			return false;
		}
		
		return true;
	}
	
	/**
	 * YV16 是 YUV:422 格式，是三个 plane,(Y)(U)(V)
	 * @param src
	 * @param width
	 * @param height
	 * @return
	 */
	public static int[] YV16ToRGB(byte[] src, int width, int height) {
		int len = width * height;
		int yStart = 0;
		int uStart = len;
		int vStart = len * 3 / 2;
		
		// RGB数组
		int[] rgbs = new int[len * 3];
		
		// RGB
		RGB rgb = new RGB();
		// 计算转换
		for (int i = 0; i < width; i++) {
			for (int j = 0; j < height; j++) {
				
				int yIdx = yStart + i * width + j;
				int uIdx = uStart + i * width / 2 + j /2;
				int vIdx = vStart + i * width / 2 + j /2;
				
				boolean to = YUV2RGB(rgb, src[yIdx], src[uIdx], src[vIdx]);
				
				// 填充
				rgbs[yIdx * 1] = rgb.r;
				rgbs[yIdx * 2] = rgb.g;
				rgbs[yIdx * 3] = rgb.b;
			}
		}
		
		return rgbs;
	}
	
	
	/**
	 * 
	 * 对 RGB 出界进行调整
	 * 
	 * @param rgb
	 * @return
	 */
	public static boolean rgbAdjust(RGB rgb) {
		rgb.r = (rgb.r < 0 ? 0 : rgb.r > 255 ? 255 : rgb.r);
		rgb.g = (rgb.g < 0 ? 0 : rgb.g > 255 ? 255 : rgb.g);
		rgb.b = (rgb.b < 0 ? 0 : rgb.b > 255 ? 255 : rgb.b);
		return true;
	}
}
