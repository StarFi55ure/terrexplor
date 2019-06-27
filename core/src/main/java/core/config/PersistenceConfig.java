package core.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

import javax.sql.DataSource;

@SuppressWarnings("ConfigurationProperties")
@Configuration
@EnableJpaRepositories(basePackages = "core.db.repositories")
public class PersistenceConfig {
    
    @ConfigurationProperties(prefix="terrexplor.datasource")
    @Bean
    public DataSource loadDataSource() {
        System.out.println("Loading datasource");
        return DataSourceBuilder.create().build();
    }
    
}
