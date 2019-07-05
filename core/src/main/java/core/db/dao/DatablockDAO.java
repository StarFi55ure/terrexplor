package core.db.dao;

import core.db.entities.Datablock;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

public class DatablockDAO implements IBaseDAO<Datablock> {
    
    @Override
    public Optional<Datablock> get(UUID primaryKey) {
        return Optional.empty();
    }
    
    @Override
    public List<Datablock> getAll() {
        return null;
    }
    
    @Override
    public void save(Datablock obj) {
    
    }
    
    @Override
    public void update(Datablock obj) {
    
    }
    
    @Override
    public void delete(Datablock obj) {
    
    }
}
