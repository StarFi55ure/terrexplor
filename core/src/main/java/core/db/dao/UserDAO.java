package core.db.dao;

import core.db.entities.UserPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Component
public class UserDAO implements IBaseDAO<UserPrincipal>, UserDetailsService {
    
    @Override
    public Optional<UserPrincipal> get(UUID primaryKey) {
        return null;
    }
    
    @Override
    public List<UserPrincipal> getAll() {
        return null;
    }
    
    public Optional<UserPrincipal> findByUsername(String username) {
        return null;
    }
    
    @Override
    public void save(UserPrincipal obj) {
    }
    
    @Override
    public void update(UserPrincipal obj) {
    
    }
    
    @Override
    public void delete(UserPrincipal obj) {
    
    }
    
    @Override
    public UserDetails loadUserByUsername(String userName) throws UsernameNotFoundException {
        var userOpt = findByUsername(userName);
    
        if (userOpt.isPresent()) {
            return new UserDetailsSupport(userOpt.get());
        } else {
            throw new UsernameNotFoundException("Username not found");
        }
    }
}
