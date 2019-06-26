package core;


import org.flywaydb.core.Flyway;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.web.servlet.WebMvcAutoConfiguration;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;

import javax.sql.DataSource;

@SpringBootApplication(scanBasePackages = {"core"})
public class MainApp extends WebMvcAutoConfiguration
{
    
    @Autowired
    private DataSource db;
    
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        SpringApplication.run(MainApp.class, args);
    }
    
    @Bean
    public CommandLineRunner commandLineRunner(ApplicationContext ctx) {
        
        migrateDatabase();
        
        return args -> {
            
            System.out.println("TerreXplor startup 2");
//            String[] beanNames = ctx.getBeanDefinitionNames();
//            Arrays.sort(beanNames);
//
//            for (String beanName: beanNames) {
//                System.out.println(beanName);
//            }
        
        };
    }
    
    private void migrateDatabase() {
        System.out.println("Running any db migrations, if any...");
        System.out.println(db.toString());
        
        Flyway flyway = Flyway.configure().dataSource(db).load();
        flyway.baseline();
        flyway.migrate();
    }
}
