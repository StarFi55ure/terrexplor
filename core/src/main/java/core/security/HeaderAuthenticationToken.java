package core.security;

import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.authority.SimpleGrantedAuthority;

import java.util.ArrayList;

public class HeaderAuthenticationToken extends UsernamePasswordAuthenticationToken {
    
    public HeaderAuthenticationToken(Object principal, Object credentials, ArrayList<SimpleGrantedAuthority> authorities) {
        super(principal, credentials, authorities);
    }
}
