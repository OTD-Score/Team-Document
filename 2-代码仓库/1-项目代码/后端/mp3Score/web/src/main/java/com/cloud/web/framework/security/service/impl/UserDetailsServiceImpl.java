package com.cloud.web.framework.security.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.cloud.web.dao.mapper.UserMapper;
import com.cloud.web.dao.model.User;
import com.cloud.web.dao.model.UserExample;
import com.cloud.web.framework.security.domain.LoginUser;
import com.cloud.web.framework.security.service.IUserDetailsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.util.CollectionUtils;

import java.util.List;

@Service
public class UserDetailsServiceImpl implements IUserDetailsService {

    @Autowired
    private UserMapper userMapper;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
//        LambdaQueryWrapper<User> lambdaQueryWrapper = new LambdaQueryWrapper<>();
//        lambdaQueryWrapper.eq(User::getUserName, username);

        UserExample userExample = new UserExample();
        UserExample.Criteria criteria = userExample.createCriteria();
        criteria.andUserNameEqualTo(username);
        List<User> users = userMapper.selectByExample(userExample);
        // 如果沒有用戶就拋出异常
        if (CollectionUtils.isEmpty(users)) {
            throw new RuntimeException("用户名或密码错误");
        }

        // 查到用户，返回信息
        return new LoginUser(users.get(0));
    }
}
