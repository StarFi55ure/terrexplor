package core.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.context.annotation.PropertySource;

import javax.sql.DataSource;

@Configuration
@PropertySource({"classpath:/persistence-${envTarget:dev}.properties"})
public class PersistenceConfig {
    
    @ConfigurationProperties(prefix="terrexplor.datasource")
    @Bean
    @Primary
    public DataSource loadDataSource() {
        System.out.println("Loading datasource");
        return DataSourceBuilder.create().build();
    }
}
