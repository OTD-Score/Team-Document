package com.cloud.web.external.klang.response;

import lombok.Data;

import java.util.Date;

/**
 * Description:
 * <p>
 * Date: 2024/6/20
 * Author: raoy
 */
@Data
public class TranscriptionResponse {

    private String job_id;

    private Date creation_date;

    private Date deletion_date;

    private boolean gen_xml;

    private boolean gen_midi;

    private boolean gen_midi_quant;

    private boolean gen_gp5;

    private boolean gen_pdf;

    private String status_endpoint_url;
}
