package com.cloud.web.framework.utils;


import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;

import java.util.Date;

public class JwtUtils {

    private static final String SECRET_KEY = "yourSecretKey";
    private static final long EXPIRATION_TIME = 86400000; // 过期时间为1天

    /**
     * 用于生成JWT。
     * 它接收一个用户ID作为参数，并使用内置的算法和秘钥生成一个包含用户ID和过期时间的签名。
     * @param userId
     * @return
     */
    public static String generateToken(String userId) {
        Date expirationDate = new Date(System.currentTimeMillis() + EXPIRATION_TIME);
        return Jwts.builder()
                .setSubject(userId)
                .setExpiration(expirationDate)
                .signWith(SignatureAlgorithm.HS512, SECRET_KEY)
                .compact();
    }

    /**
     * 用于从JWT中提取用户ID。
     * 它接收一个JWT令牌作为参数，并解析其中的主题（主体）部分来获取用户ID。
     * @param token
     * @return
     */
    public static String getUserIdFromToken(String token) {
        Claims claims = Jwts.parser()
                .setSigningKey(SECRET_KEY)
                .parseClaimsJws(token)
                .getBody();

        return claims.getSubject();
    }

    /**
     * 用于验证JWT的有效性。
     * 它接收一个JWT令牌作为参数，并解析和验证签名。
     * 如果令牌有效且未过期，则返回true；否则返回false。
     * @param token
     * @return
     */
    public static boolean isTokenValid(String token) {
        try {
            Jwts.parser().setSigningKey(SECRET_KEY).parseClaimsJws(token);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}