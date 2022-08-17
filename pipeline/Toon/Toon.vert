#version 130

varying float intensity;

in vec3 position;
in vec3 normal;
uniform mat4 MVP;

void main(void) 
{   
    gl_Position = MVP * vec4(position,1.0);
    vec3 lightDir = normalize(vec3(10.0,0.0,10.0));
    intensity = dot(lightDir,normal);
    
}
