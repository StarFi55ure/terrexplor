package core.services;

import core.db.dao.UserAuthorizationDAO;
import core.db.dao.UserDAO;
import core.db.entities.UserPrincipal;
import org.apache.commons.codec.digest.DigestUtils;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.Optional;

import static org.apache.commons.codec.digest.MessageDigestAlgorithms.SHA_256;

//@Service
public class AuthService {
    
    @Autowired
    private UserDAO userDAO;
    
    @Autowired
    private UserAuthorizationDAO authorizationDAO;
    
    public Optional<String> login(String username, String password) {
//        var userPrincipalOpt = userPrincipalRepository.findByUsername(username);
//        System.out.println(userPrincipalOpt);
//
//        if (userPrincipalOpt.isPresent()) {
//            var userPrincipal = userPrincipalOpt.get();
//
//            if (isUserPrincipalPasswordValid(userPrincipal, password)) {
//                return Optional.empty();
//            } else {
//                throw new BadCredentialsException("");
//            }
//        } else {
//            throw new UsernameNotFoundException("");
//        }
        return Optional.empty();
    
    }
    
    public Optional<UserPrincipal> findByToken(String token) {
        return authorizationDAO.get(token)
            .flatMap(userAuth -> userDAO.get(userAuth.getUserid()));
    }
    
    private boolean isUserPrincipalPasswordValid(UserPrincipal userPrincipal, String password) {
        var hexdigest = new DigestUtils(SHA_256).digestAsHex(userPrincipal.getSalt() + password);
        return hexdigest.equals(userPrincipal.getPassword());
    }
    
}
