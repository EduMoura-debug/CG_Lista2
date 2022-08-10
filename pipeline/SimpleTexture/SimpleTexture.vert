#version 130

in vec3 position;
in vec3 color;

out vec3 colorToFragmentShader;
uniform mat4 MVP;

void main(void) 
{
    gl_Position = MVP*vec4(position,1.0);
    colorToFragmentShader = color;
}
