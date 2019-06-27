package core.api.resources;

import javax.ws.rs.GET;
import javax.ws.rs.Path;

@Path("config")
public interface ConfigApi {
    
    @GET
    @Path("userconfig")
    String getCurrentUserConfig();
}
