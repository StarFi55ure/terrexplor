package core.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class SandboxController {
    
    @RequestMapping("/sandbox")
    public @ResponseBody String getIndex(Model model) {
        
//        var uM = session.getMapper(UserMapper.class);
//        var user = uM.selectOne(UUID.fromString("e894a02a-f99c-469c-adde-49363837a706"));
    
//        System.out.println(user.get().getDatecreated());
//        throw new ResponseStatusException(HttpStatus.FORBIDDEN, "unauth");
        
        return "sandbox controller";
    }
}
