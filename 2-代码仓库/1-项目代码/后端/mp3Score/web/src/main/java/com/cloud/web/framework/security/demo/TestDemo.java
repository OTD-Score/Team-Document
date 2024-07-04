package com.cloud.web.framework.security.demo;

import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class TestDemo {
    public static void main(String[] args) {
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
        String encode = passwordEncoder.encode("123123");
        System.out.println(encode);
    }

}
