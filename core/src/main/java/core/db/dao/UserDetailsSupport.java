package core.db.dao;

import core.db.entities.UserPrincipal;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class UserDetailsSupport implements UserDetails {
    
    private final UserPrincipal userPrincipalEntity;
    protected List<GrantedAuthority> authorityList;
    
    public UserDetailsSupport(UserPrincipal userPrincipalEntity) {
        this.authorityList = new ArrayList<>();
        this.userPrincipalEntity = userPrincipalEntity;
    }
    
    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return authorityList;
    }
    
    @Override
    public String getPassword() {
        return null;
    }
    
    @Override
    public String getUsername() {
        return null;
    }
    
    @Override
    public boolean isAccountNonExpired() {
        return false;
    }
    
    @Override
    public boolean isAccountNonLocked() {
        return false;
    }
    
    @Override
    public boolean isCredentialsNonExpired() {
        return false;
    }
    
    @Override
    public boolean isEnabled() {
        return false;
    }
    
    public UserPrincipal getUserEntity() {
        return userPrincipalEntity;
    }
}
