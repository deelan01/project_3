-- Table: public.earthquake

DROP TABLE IF EXISTS public.earthquake;

CREATE TABLE IF NOT EXISTS public.earthquake
(
    id_number integer NOT NULL DEFAULT nextval('earthquake_id_number_seq'::regclass),
    time_ date,
    lat numeric(100,0),
    "long" numeric(100,0),
    depth_ numeric(10,2),
    mag numeric(10,2),
    mag_type character varying(10) COLLATE pg_catalog."default",
    id_num character varying(50) COLLATE pg_catalog."default" NOT NULL,
    updated date,
    place character varying(100) COLLATE pg_catalog."default",
    type_ character varying(100) COLLATE pg_catalog."default",
    horizonial_error character varying(100) COLLATE pg_catalog."default",
    depth_error character varying(100) COLLATE pg_catalog."default",
    magnitude_source character varying(10) COLLATE pg_catalog."default",
    location_source character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT earthquake_pkey PRIMARY KEY (id_num)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.earthquake
    OWNER to postgres;