package core.controllers.api;

import core.api.data.AuthLoginReq;
import core.api.data.AuthLoginRes;
import core.services.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.AuthenticationException;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

//@RestController
//@RequestMapping("/api")
public class Auth {
    
    @Autowired
    private AuthService authService;
    
    @PostMapping(value = "login",  consumes = "application/json")
    public ResponseEntity<AuthLoginRes> loginUser(@RequestBody AuthLoginReq loginReq) {
        try {
            var authTokenOpt = authService.login(loginReq.getUsername(), loginReq.getPassword());
            var authTokenRes = new AuthLoginRes();
            authTokenRes.setAuthToken(authTokenOpt.orElse("None"));
            return new ResponseEntity<>(authTokenRes, HttpStatus.OK);
        } catch (AuthenticationException ex) {
            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED, ex.getMessage());
        }
    }
    
    @GetMapping("authMe")
    public ResponseEntity<String> authMe() {
        return new ResponseEntity<>("{\"mykey\": \"This is authenticated\"}", HttpStatus.OK);
    }
}
