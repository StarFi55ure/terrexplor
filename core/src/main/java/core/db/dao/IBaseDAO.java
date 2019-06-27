package core.db.dao;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

/**
 * Base interface for all DAO objects
 *
 * @param <T>
 */
public interface IBaseDAO<T> {
    Optional<T> get(UUID primaryKey);
    List<T> getAll();
    void save(T obj);
    void update(T obj);
    void delete(T obj);
}
