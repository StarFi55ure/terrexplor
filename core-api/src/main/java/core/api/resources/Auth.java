package core.api.resources;

import core.api.data.AuthLoginReq;
import core.api.data.AuthLoginRes;

import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/")
public interface Auth {
    
    @POST
    @Path("/login")
    @Produces(MediaType.APPLICATION_JSON)
    AuthLoginRes loginUser(AuthLoginReq loginReq);
}
