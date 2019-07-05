package core.db.entities;

import lombok.Data;
import org.apache.ibatis.type.Alias;

import java.time.LocalDateTime;
import java.util.UUID;

@Data
@Alias("Datablock")
public class Datablock {
    
    private UUID datablockid;
    private String md5;
    private long size;
    private LocalDateTime datecreated;
    private boolean active;
    
}
