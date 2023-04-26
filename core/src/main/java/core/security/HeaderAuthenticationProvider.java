package core.security;

import core.services.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.authentication.dao.AbstractUserDetailsAuthenticationProvider;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Component;

import java.util.Optional;

//@Component
public class HeaderAuthenticationProvider extends AbstractUserDetailsAuthenticationProvider {
    
    @Autowired
    private AuthService authService;
    
    @Override
    protected void additionalAuthenticationChecks(UserDetails userDetails, UsernamePasswordAuthenticationToken usernamePasswordAuthenticationToken) throws AuthenticationException {
    
    }
    
    @Override
    protected UserDetails retrieveUser(String username,
                                       UsernamePasswordAuthenticationToken authToken) throws AuthenticationException {
        var token = authToken.getCredentials();
        return Optional
            .ofNullable(token)
            .map(String::valueOf)
            .flatMap(authService::findByToken)
            .orElseThrow(() -> new UsernameNotFoundException("No user with token: " + token));
    }
}
