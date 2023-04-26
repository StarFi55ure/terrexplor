package core;


import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.web.servlet.WebMvcAutoConfiguration;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;

@SpringBootApplication(scanBasePackages = {"core"})
public class MainApp extends WebMvcAutoConfiguration
{
    
    public static void main( String[] args )
    {
        SpringApplication.run(MainApp.class, args);
    }
    
    @Bean
    public CommandLineRunner commandLineRunner(ApplicationContext ctx) {
        
        
        return args -> {
            
            System.out.println("TerreXplor Core");
//            String[] beanNames = ctx.getBeanDefinitionNames();
//            Arrays.sort(beanNames);
//
//            for (String beanName: beanNames) {
//                System.out.println(beanName);
//            }
        
        };
    }
}
