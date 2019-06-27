package core.db.repositories;

import core.db.entities.UserPrincipal;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;
import java.util.UUID;

@Repository
public interface UserPrincipalRepository extends CrudRepository<UserPrincipal, UUID> {
    
    Optional<UserPrincipal> findByUsername(String username);
}
