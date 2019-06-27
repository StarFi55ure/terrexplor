package core.db.entities;

import java.time.OffsetDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.UUID;

public class UserPrincipalAuthToken extends BaseEntity {
    
    private UUID userauthid;
    private UUID userid;
    private OffsetDateTime expire;
    private String token;
    
    public UUID getUserauthid() {
        return userauthid;
    }
    
    public void setUserauthid(UUID userauthid) {
        this.userauthid = userauthid;
    }
    
    public UUID getUserid() {
        return userid;
    }
    
    public void setUserid(UUID userid) {
        this.userid = userid;
    }
    
    public ZonedDateTime getExpire() {
        return expire.atZoneSameInstant(ZoneId.systemDefault());
    }
    
    public void setExpire(OffsetDateTime expire) {
        this.expire = expire;
    }
    
    public String getToken() {
        return token;
    }
    
    public void setToken(String token) {
        this.token = token;
    }
}
