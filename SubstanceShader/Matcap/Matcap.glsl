import lib-sparse.glsl

//: param auto channel_basecolor
uniform SamplerSparse basecolor_tex;

void shade(V2F inputs)
{
    vec3 basecolor = textureSparse(basecolor_tex,inputs.sparse_coord).rgb;
    diffuseShadingOutput(basecolor);
}

