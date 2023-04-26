package core.controllers.api;

import core.db.dao.UserDAO;
import core.db.entities.UserPrincipal;
import core.services.AuthService;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.context.TestConfiguration;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Primary;
import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.web.servlet.MockMvc;

import javax.sql.DataSource;
import javax.ws.rs.core.MediaType;
import java.util.Optional;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@ExtendWith(SpringExtension.class)
@WebMvcTest(Auth.class)
@Disabled
public class AuthTest {
    // TODO: might need to refactor fixture into Before method, must reset objects
    
    @TestConfiguration
    static class AuthImplTestContextConfiguration {
    
        @Bean
        @Primary
        public DataSource getDS() {
            return mock(DataSource.class);
        }
        
        @Bean
        public AuthenticationProvider getAuthProvider() {
            return mock(AuthenticationProvider.class);
        }
        
        @Bean
        public UserDAO getUserDAO() {
            return mock(UserDAO.class);
        }
    
    }
    
    @MockBean
    private AuthService authService;
    
    @Autowired
    private MockMvc mockMvc;
    
    @Test
    public void whenLoginCorrect_thenAuthTokenReturned() throws Exception {
    
        var testUser = new UserPrincipal();
        testUser.setUsername("admin");
        testUser.setPassword("admin");
        Optional<UserPrincipal> testUserOptional = Optional.of(testUser);
        
        var testAuthToken = "7a6b6052-5ba5-46c8-bfc5-5e3cc292a512";
        
        when(authService.login(testUser.getUsername(), testUser.getPassword())).thenReturn(Optional.of(testAuthToken));
        
        mockMvc.perform(post("/api/login")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"username\": \"admin\", \"password\": \"admin\"}"))
            .andExpect(status().isOk());
        //TODO: add check for existence of auth token in payload
    }
    
    @Test
    public void whenLoginWrongPassword_then401Returned() throws Exception {
    
        var testUser = new UserPrincipal();
        testUser.setUsername("admin");
        testUser.setPassword("admin-wrong");
        Optional<UserPrincipal> testUserOptional = Optional.of(testUser);
    
        when(authService.login(testUser.getUsername(), testUser.getPassword())).thenThrow(new BadCredentialsException(""));
        
        mockMvc.perform(post("/api/login")
            .contentType(MediaType.APPLICATION_JSON)
            .content("{\"username\": \"admin\", \"password\": \"admin-wrong\"}"))
            .andExpect(status().isUnauthorized());
        
        //TODO: add check for error message
    }
    
    @Test
    public void whenLoginWrongUsername_then401Returned() throws Exception {
        
        var testUser = new UserPrincipal();
        testUser.setUsername("admin-doesnt-exist");
        testUser.setPassword("admin");
        Optional<UserPrincipal> testUserOptional = Optional.of(testUser);
    
        var testAuthToken = "7a6b6052-5ba5-46c8-bfc5-5e3cc292a512";
    
        when(authService.login(testUser.getUsername(), testUser.getPassword())).thenThrow(new UsernameNotFoundException(""));
        
        mockMvc.perform(post("/api/login")
            .contentType(MediaType.APPLICATION_JSON)
            .content("{\"username\": \"admin-doesnt-exist\", \"password\": \"admin\"}"))
            .andExpect(status().isUnauthorized());
    
    }
}
