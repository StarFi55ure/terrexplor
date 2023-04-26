package core.db.dao;

import core.db.entities.UserPrincipalAuthToken;
import org.apache.commons.lang3.NotImplementedException;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Component
public class UserAuthorizationDAO implements IBaseDAO<UserPrincipalAuthToken> {
    
    @Override
    public Optional<UserPrincipalAuthToken> get(UUID primaryKey) {
        throw new NotImplementedException("UserAuthorizationDAO.get(UUID)");
    }
    
    public Optional<UserPrincipalAuthToken> get(String token) {
        return null;
    }
    
    @Override
    public List<UserPrincipalAuthToken> getAll() {
        return null;
    }
    
    @Override
    public void save(UserPrincipalAuthToken obj) {
    }
    
    @Override
    public void update(UserPrincipalAuthToken obj) {
    
    }
    
    @Override
    public void delete(UserPrincipalAuthToken obj) {
    
    }
}
