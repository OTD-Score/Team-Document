package com.cloud.web.utils;

import cn.hutool.http.HttpRequest;
import cn.hutool.http.HttpResponse;
import cn.hutool.http.HttpUtil;
import com.alibaba.fastjson.JSONObject;

import java.util.HashMap;

/**
 * Description:
 * <p>
 * Date: 2024/6/20
 * Author: raoy
 */
public class HuToolHttpUtil {

    public static String hutoolGet(String url, HashMap<String, Object> params) {
        // 请求头
        HashMap<String, String> headers = new HashMap<>();

        return HttpUtil.createGet(url).addHeaders(headers).form(params).execute().body();
    }

    public static String hutoolGet(String url, HashMap<String, String> headers, HashMap<String, Object> params) {

        return HttpUtil.createGet(url).addHeaders(headers).form(params).execute().body();
    }

    public static HttpResponse hutoolGetHttpResponse(String url, HashMap<String, String> headers, HashMap<String, Object> params) {
        HttpResponse httpResponse = HttpUtil.createGet(url).addHeaders(headers).form(params).execute();
        return httpResponse;
    }

    public static String hutoolPost(String url, HashMap<String, Object> params) {
        // 请求头
        HashMap<String, String> headers = new HashMap<>();

        // 参数转JSON字符串
        String json = JSONObject.toJSONString(params);
        return HttpRequest.post(url).addHeaders(headers).body(json).execute().body();
    }

    public static String hutoolPost(String url, HashMap<String, String> headers, HashMap<String, Object> params) {

        // 参数转JSON字符串
//        String json = JSONObject.toJSONString(params);
        return HttpRequest.post(url).addHeaders(headers).form(params).execute().body();
    }

    public static String hutoolPost(String url, HashMap<String, String> headers, HashMap<String, Object> params, byte[] fileBytes, String name, String fileName) {

        // 参数转JSON字符串
//        String json = JSONObject.toJSONString(params);
        HttpRequest form = HttpRequest.post(url).addHeaders(headers).form(params).form(name, fileBytes, fileName);
        return form.execute().body();
    }
}
