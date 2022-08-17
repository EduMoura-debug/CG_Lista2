#version 130

varying float intensity;

in vec3 position;
uniform mat4 MVP;


void main(void) 
{   
    gl_Position = MVP * vec4(position,1.0);
    
    vec3 lightDir = normalize(vec3(gl_LightSource[0].position));
	intensity = dot(lightDir,gl_Normal);

}