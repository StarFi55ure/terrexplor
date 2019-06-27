package core.db.entities;

import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.GenericGenerator;

import javax.persistence.Column;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.MappedSuperclass;
import java.time.OffsetDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.UUID;

@MappedSuperclass
public class BaseEntity {
    
    @Id
    @GeneratedValue(generator = "UUID")
    @GenericGenerator(
        name = "UUID",
        strategy = "org.hibernate.id.UUIDGenerator"
    )
    @Column(name = "id", updatable = false, nullable = false)
    @ColumnDefault("uuid_generate_v4()")
    protected UUID id;
    
    @Column(updatable = false, nullable = false)
    @ColumnDefault("now()")
    protected OffsetDateTime datecreated;
    
    @Column(nullable = false)
    @ColumnDefault("true")
    protected Boolean active;
    
    public UUID getId() {
        return id;
    }
    
    public void setId(UUID id) {
        this.id = id;
    }
    
    public OffsetDateTime getDatecreated() {
        return datecreated;
    }
    
    public ZonedDateTime getZonedDatecreated() {
        return datecreated.atZoneSameInstant(ZoneId.systemDefault());
    }
    
    public Boolean getActive() {
        return active;
    }
    
    public void setActive(Boolean active) {
        this.active = active;
    }
}
