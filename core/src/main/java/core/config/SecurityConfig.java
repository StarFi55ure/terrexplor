package core.config;

import core.security.HeaderAuthenticationFilter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpStatus;
import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.builders.WebSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.AuthenticationEntryPoint;
import org.springframework.security.web.authentication.AnonymousAuthenticationFilter;
import org.springframework.security.web.authentication.HttpStatusEntryPoint;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;
import org.springframework.security.web.util.matcher.OrRequestMatcher;
import org.springframework.security.web.util.matcher.RequestMatcher;

//@Configuration
//@EnableWebSecurity
//@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    
    private static final RequestMatcher PROTECTED_API_URLS = new OrRequestMatcher(
        new AntPathRequestMatcher("/api/**")
    );
    
    AuthenticationProvider provider;
    
    public SecurityConfig(AuthenticationProvider provider) {
        super();
        this.provider = provider;
    }
    
//    @Override
//    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
//        auth.authenticationProvider(this.provider);
//    }
    
//    @Override
//    public void configure(WebSecurity web) throws Exception {
//        System.out.println("Config websecurity");
//        web.ignoring().antMatchers("/api/login", "/sandbox", "/");
//    }
    
//    @Override
//    protected void configure(HttpSecurity http) throws Exception {
//        System.out.println("Configure http security");
//        http.sessionManagement()
//            .sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED)
//            .and()
//            .exceptionHandling()
//            .authenticationEntryPoint(new HttpStatusEntryPoint(HttpStatus.UNAUTHORIZED))
//            .and()
//            .authenticationProvider(provider)
//            .addFilterBefore(authenticationFilter(), AnonymousAuthenticationFilter.class)
//            .authorizeRequests()
//            .requestMatchers(PROTECTED_API_URLS)
//            .authenticated()
//            .and()
//            .csrf().disable()
//            .formLogin().disable()
//            .httpBasic().disable()
//            .logout().disable();
//
//    }
    
    
//    protected HeaderAuthenticationFilter authenticationFilter() throws Exception {
//        final var authenticationFilter = new HeaderAuthenticationFilter(PROTECTED_API_URLS);
//        authenticationFilter.setAuthenticationManager(authenticationManager());
//        return authenticationFilter;
//    }
//
//    @Bean
//    public AuthenticationEntryPoint entryPoint() {
//        return new HttpStatusEntryPoint(HttpStatus.FORBIDDEN);
//    }

}
