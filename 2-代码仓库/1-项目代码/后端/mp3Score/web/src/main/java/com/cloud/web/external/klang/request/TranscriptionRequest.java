package com.cloud.web.external.klang.request;

import lombok.Data;
import org.springframework.web.multipart.MultipartFile;

/**
 * Description:
 * <p>
 * Date: 2024/6/20
 * Author: raoy
 */
@Data
public class TranscriptionRequest {

    private MultipartFile file;

    private String outputs;
}
