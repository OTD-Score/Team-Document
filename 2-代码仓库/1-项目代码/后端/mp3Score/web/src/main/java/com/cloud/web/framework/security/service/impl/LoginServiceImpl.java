package com.cloud.web.framework.security.service.impl;

import com.cloud.web.dao.model.User;
import com.cloud.web.domain.R;
import com.cloud.web.framework.redis.RedisCache;
import com.cloud.web.framework.security.domain.LoginUser;
import com.cloud.web.framework.security.service.ILoginService;
import com.cloud.web.framework.utils.JwtUtils;
import org.apache.commons.lang3.ObjectUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

@Service
public class LoginServiceImpl implements ILoginService {

    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    private RedisCache redisCache;

    @Override
    public R login(User user) {
        // Authentication authenticate 进行用户认证
        UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(user.getUserName(), user.getPassword());
        Authentication authenticate = authenticationManager.authenticate(authenticationToken);

        // 认证失败，返回异常
        if (ObjectUtils.isEmpty(authenticate)) {
            throw new RuntimeException("登录失败...");
        }
        // 认证通过，生成jwt，返回
        LoginUser loginUser = (LoginUser) authenticate.getPrincipal();
        String userId = loginUser.getUser().getId().toString();
        // 根据用户ID生成jwt
        String jwt = JwtUtils.generateToken(userId);
        Map<String, String> map = new HashMap<>();
        map.put("token", jwt);
        // 把完整的用户信息存入redis，userId作为key
        redisCache.setCacheObject("login:" + userId, loginUser, 24, TimeUnit.HOURS);
        String username = loginUser.getUser().getUserName().toString();
        return R.ok(map, "登录成功，欢迎：" + username);
    }

    @Override
    public R logout() {
        // 获取SecurityContextHolder中的用户ID
        UsernamePasswordAuthenticationToken authenticationToken = (UsernamePasswordAuthenticationToken) SecurityContextHolder.getContext().getAuthentication();
        LoginUser loginUser = (LoginUser) authenticationToken.getPrincipal();
        String userId = loginUser.getUser().getId();
        // 删除redis中的值
        redisCache.deleteObject("login:" + userId);
        return R.ok(null, "注销成功");
    }
}
