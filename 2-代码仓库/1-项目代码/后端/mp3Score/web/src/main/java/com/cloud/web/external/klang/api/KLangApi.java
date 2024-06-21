package com.cloud.web.external.klang.api;

import cn.hutool.http.HttpResponse;
import com.alibaba.fastjson.JSON;
import com.cloud.web.domain.R;
import com.cloud.web.external.klang.response.JobStatus;
import com.cloud.web.external.klang.response.TranscriptionResponse;
import com.cloud.web.utils.HuToolHttpUtil;
import org.apache.commons.lang3.StringUtils;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.OutputStream;
import java.util.HashMap;

/**
 * Description:
 * <p>
 * Date: 2024/6/20
 * Author: raoy
 */
@Service
public class KLangApi {

    public R<JobStatus> getJobStatus(String jobId) {
        String url = "https://api.klang.io/job/" + jobId + "/status";
        HashMap<String, String> headers = new HashMap<>();
        headers.put("Kl-Api-Key", "0xkl-ad5e4946cfaf48c6969e0923977791cd");
        headers.put("accept", "application/json");

        String response = HuToolHttpUtil.hutoolGet(url, headers, new HashMap<>());

        JobStatus jobStatus = new JobStatus();
        if (StringUtils.isNotEmpty(response)) {
            jobStatus = JSON.parseObject(response, JobStatus.class);
            return R.ok(jobStatus);
        }
        return R.fail();
    }

    public R<TranscriptionResponse> transcription(String model, String output, MultipartFile file) {
        String url = "https://api.klang.io/transcription?model=" + model;
        HashMap<String, String> headers = new HashMap<>();
        headers.put("Kl-Api-Key", "0xkl-ad5e4946cfaf48c6969e0923977791cd");
        headers.put("accept", "application/json");
        headers.put("Content-Type", "multipart/form-data");

        String response = null;
        try {
            HashMap<String, Object> params = new HashMap<>();
            params.put("outputs", output);
            response = HuToolHttpUtil.hutoolPost(url, headers, params, file.getBytes(), "file", file.getOriginalFilename());
        } catch (IOException e) {
            return R.fail(e.getMessage());
        }

        TranscriptionResponse transcriptionResponse = new TranscriptionResponse();
        if (StringUtils.isNotEmpty(response)) {
            transcriptionResponse = JSON.parseObject(response, TranscriptionResponse.class);
            return R.ok(transcriptionResponse);
        }
        return R.fail();
    }

    public void download(String jobId, String fileType, HttpServletResponse httpServletResponse) {
        String url = "https://api.klang.io/job/" + jobId + "/" + fileType;
        HashMap<String, String> headers = new HashMap<>();
        headers.put("Kl-Api-Key", "0xkl-ad5e4946cfaf48c6969e0923977791cd");
        headers.put("accept", "application/json");

        HttpResponse response = HuToolHttpUtil.hutoolGetHttpResponse(url, headers, new HashMap<>());


        // try代码块写入响应内容即可！
        try {
            // 设置响应类型
            httpServletResponse.setContentType("application/octet-stream");
            // 设置响应输出流
            OutputStream out = httpServletResponse.getOutputStream();
            // 写入内容
            long l = response.writeBody(out, false, null);
            // 执行写入 刷新此输出流并强制写入任何缓冲的输出字节
            out.flush();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
