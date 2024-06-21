package com.cloud.web.controller;

import com.cloud.web.dao.mapper.UserMapper;
import com.cloud.web.dao.model.User;
import com.cloud.web.dao.model.UserExample;
import com.cloud.web.domain.R;
import com.cloud.web.framework.security.service.ILoginService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.util.CollectionUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class LoginController {

    @Autowired
    private UserMapper userMapper;

    @Autowired
    private ILoginService loginService;

    @RequestMapping("/login-success")
    public String loginSuccess() {

        return "登录成功";
    }

    @RequestMapping("/r/r1")
    @PreAuthorize("hasAuthority('p1')")//拥有p1权限方可访问
    public String r1() {
        return "访问r1资源";
    }

    @RequestMapping("/r/r2")
    @PreAuthorize("hasAuthority('p2')")//拥有p1权限方可访问
    public String r2() {
        return "访问r2资源";
    }

    @PostMapping("/login")
    public R loginSuccess(@RequestBody User user){
        return loginService.login(user);
    }

    @RequestMapping("/user/{id}")
    public R getuser(@PathVariable("id") String id) {
        UserExample userExample = new UserExample();
        UserExample.Criteria criteria = userExample.createCriteria();
        criteria.andIdEqualTo(id);
        List<User> users = userMapper.selectByExample(userExample);
        // 如果沒有用戶就拋出异常
        if (CollectionUtils.isEmpty(users)) {
            throw new RuntimeException("用户名或密码错误");
        }
        return R.ok(users.get(0));
    }

    @RequestMapping(method = RequestMethod.POST, value = "/logout")
    public R logout(){
        return loginService.logout();
    }


    @RequestMapping(method = RequestMethod.GET, value = "/logout/success")
    public R logoutSuccess(){
        return R.ok("logout success");
    }

}
