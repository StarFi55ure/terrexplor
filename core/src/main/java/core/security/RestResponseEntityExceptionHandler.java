package core.security;

import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.server.ResponseStatusException;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

//@ControllerAdvice
public class RestResponseEntityExceptionHandler extends ResponseEntityExceptionHandler {
    
    @ExceptionHandler({ResponseStatusException.class})
    public ResponseEntity<Object> handleUnauthorized(ResponseStatusException ex, WebRequest req) {
        System.out.println("Global Exception handler");
        return handleExceptionInternal(ex, "Access Denied", new HttpHeaders(),
            HttpStatus.UNAUTHORIZED, req);
    }
}
