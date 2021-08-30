package core.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;

@SuppressWarnings("ConfigurationProperties")
@Configuration
public class PersistenceConfig {
    
    @ConfigurationProperties(prefix="terrexplor.datasource")
    @Bean
    public DataSource loadDataSource() {
        System.out.println("Loading datasource");
        return DataSourceBuilder.create().build();
    }
    
}
