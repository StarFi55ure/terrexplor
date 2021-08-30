package core.db.entities;

import java.time.OffsetDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.UUID;

public abstract class BaseEntity {
    
    protected UUID id;
    protected OffsetDateTime created;
    protected OffsetDateTime modified;
    protected Boolean active;
    
    public UUID getId() {
        return id;
    }
    
    public void setId(UUID id) {
        this.id = id;
    }
    
    public OffsetDateTime getCreated() {
        return created;
    }
    
    public void setCreated(OffsetDateTime created) {
        this.created = created;
    }
    
    public OffsetDateTime getModified() {
        return modified;
    }
    
    public void setModified(OffsetDateTime modified) {
        this.modified = modified;
    }
    
    public ZonedDateTime getZonedCreated() {
        return created.atZoneSameInstant(ZoneId.systemDefault());
    }
    
    public Boolean getActive() {
        return active;
    }
    
    public void setActive(Boolean active) {
        this.active = active;
    }
}
