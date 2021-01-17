CREATE TABLE public.usuario
(
    id_usuario serial NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL,
    PRIMARY KEY (id_usuario)
);

ALTER TABLE public.usuario
    OWNER to postgres;