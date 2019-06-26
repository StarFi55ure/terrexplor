package core.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class SandboxController {
    
    @RequestMapping("/")
    public String getIndex(Model model) {
        return "pages/index";
    }
}
