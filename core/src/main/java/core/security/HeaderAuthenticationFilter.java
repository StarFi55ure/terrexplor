package core.security;

import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.authentication.AbstractAuthenticationProcessingFilter;
import org.springframework.security.web.util.matcher.RequestMatcher;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Arrays;
import java.util.Optional;

public class HeaderAuthenticationFilter extends AbstractAuthenticationProcessingFilter {
    
    public HeaderAuthenticationFilter(RequestMatcher requiresAuth) {
        super(requiresAuth);
    }
    
    @Override
    public Authentication attemptAuthentication(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse) throws AuthenticationException, IOException, ServletException {
        Optional<String> tokenOptional = Optional.ofNullable(httpServletRequest.getHeader("X-TX-AuthToken"));
        if (tokenOptional.isPresent()) {
            var token = tokenOptional.get().trim();
    
            Authentication reqAuthToken = new UsernamePasswordAuthenticationToken(token, token);
            return getAuthenticationManager().authenticate(reqAuthToken);
        } else {
//            throw new BadCredentialsException("Bad Credentials");
            var rejected = new UsernamePasswordAuthenticationToken("", "", Arrays.asList());
            return rejected;
        }
    }
    
    @Override
    protected void successfulAuthentication(HttpServletRequest request, HttpServletResponse response, FilterChain chain, Authentication authResult) throws IOException, ServletException {
        SecurityContextHolder.getContext().setAuthentication(authResult);
        chain.doFilter(request, response);
    }
    
    @Override
    protected void unsuccessfulAuthentication(HttpServletRequest request, HttpServletResponse response, AuthenticationException failed) throws IOException, ServletException {
        //super.unsuccessfulAuthentication(request, response, failed);
        System.out.println("Unsuccessful authentication");
        response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
        response.getWriter().println("Unauthorized: " + failed.getMessage());
    }
}
