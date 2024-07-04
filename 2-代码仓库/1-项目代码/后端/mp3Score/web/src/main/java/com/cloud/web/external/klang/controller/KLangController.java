package com.cloud.web.external.klang.controller;

import com.cloud.web.domain.R;
import com.cloud.web.external.klang.api.KLangApi;
import com.cloud.web.external.klang.response.JobStatus;
import com.cloud.web.external.klang.response.TranscriptionResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletResponse;

/**
 * Description:
 * <p>
 * Date: 2024/6/20
 * Author: raoy
 */
@RestController
@RequestMapping("/klang")
public class KLangController {

    @Autowired
    private KLangApi kLangApi;

    @RequestMapping(method = RequestMethod.GET, value = "/getJobStatus")
    public R<JobStatus> getJobStatus(@RequestParam("jobId") String jobId) {
        return kLangApi.getJobStatus(jobId);
    }

    @RequestMapping(method = RequestMethod.POST, value = "/transcription")
    public R<TranscriptionResponse> transcription(@RequestParam("model") String model,
                                                  @RequestParam("output") String output,
                                                  @RequestParam("file") MultipartFile file) {
        return kLangApi.transcription(model, output, file);
    }

    @RequestMapping(method = RequestMethod.GET, value = "/download")
    public void download(@RequestParam("jobId") String jobId,
                                 @RequestParam("fileType") String fileType,
                                 HttpServletResponse httpServletResponse) {
        kLangApi.download(jobId, fileType, httpServletResponse);
    }
}
