package core.db.utils;

import org.hibernate.boot.model.naming.Identifier;
import org.hibernate.engine.jdbc.env.spi.JdbcEnvironment;
import org.springframework.boot.orm.jpa.hibernate.SpringPhysicalNamingStrategy;

import java.io.Serializable;

public class CustomPhysicalNamingStrategy extends SpringPhysicalNamingStrategy implements Serializable {

    @Override
    public Identifier toPhysicalTableName(Identifier name, JdbcEnvironment context) {
        return new Identifier(name.getText().toLowerCase(), name.isQuoted());
    }

//    @Override
//    public Identifier toPhysicalColumnName(Identifier name, JdbcEnvironment context) {
//        return new Identifier(name.getText(), name.isQuoted());
//    }
}
