package com.cloud.web.framework.security.service;

import com.cloud.web.dao.model.User;
import com.cloud.web.domain.R;

public interface ILoginService {

    R login(User user);

    R logout();
}
