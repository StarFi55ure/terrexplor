package core.config;

import org.springframework.context.annotation.Configuration;

import javax.inject.Named;

@Configuration
public class FilesystemStorageConfig {

    @Named("fileStorePath")
    String getFileSystemStoragePath() {
        return "/home/julian/projects/terrexplor/filestore";
    }
    
}
