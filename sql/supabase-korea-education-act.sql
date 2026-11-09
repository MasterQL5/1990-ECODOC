-- Korea Higher Education Development Act: modest long-run talent boost for firms partnered with universities.
-- Adds 0.2 to 1.5 percentage points a year to their normal projected change, phased in 1991-92, full from 1993. Other Korean companies are unchanged.
-- Needs the page version with per-year stock changes (already deployed). Paste into Supabase > SQL Editor and run once.
insert into public.kv (k, v) values
  ('co/Samsung Electronics', '{"yg": {"1991": 8.45, "1992": 8.9, "1993": 9.5, "1994": 9.5, "1995": 9.5, "1996": 9.5, "1997": 9.5, "1998": 9.5, "1999": 9.5, "2000": 9.5}}'::jsonb),
  ('co/Hyundai Motor', '{"yg": {"1991": 5.3, "1992": 5.6, "1993": 6.0, "1994": 6.0, "1995": 6.0, "1996": 6.0, "1997": 6.0, "1998": 6.0, "1999": 6.0, "2000": 6.0}}'::jsonb),
  ('co/Kia Motors', '{"yg": {"1991": 5.15, "1992": 5.3, "1993": 5.5, "1994": 5.5, "1995": 5.5, "1996": 5.5, "1997": 5.5, "1998": 5.5, "1999": 5.5, "2000": 5.5}}'::jsonb),
  ('co/Lucky', '{"yg": {"1991": 4.24, "1992": 4.48, "1993": 4.8, "1994": 4.8, "1995": 4.8, "1996": 4.8, "1997": 4.8, "1998": 4.8, "1999": 4.8, "2000": 4.8}}'::jsonb),
  ('co/Pohang Iron & Steel (POSCO)', '{"yg": {"1991": -1.76, "1992": -1.52, "1993": -1.2, "1994": -1.2, "1995": -1.2, "1996": -1.2, "1997": -1.2, "1998": -1.2, "1999": -1.2, "2000": -1.2}}'::jsonb),
  ('co/SK (Sunkyong)', '{"yg": {"1991": 3.24, "1992": 3.48, "1993": 3.8, "1994": 3.8, "1995": 3.8, "1996": 3.8, "1997": 3.8, "1998": 3.8, "1999": 3.8, "2000": 3.8}}'::jsonb),
  ('co/Miscellaneous: other South Korea listed companies', '{"yg": {"1991": 4.06, "1992": 4.12, "1993": 4.2, "1994": 4.2, "1995": 4.2, "1996": 4.2, "1997": 4.2, "1998": 4.2, "1999": 4.2, "2000": 4.2}}'::jsonb)
on conflict (k) do update set v = coalesce(public.kv.v, '{}'::jsonb) || excluded.v, updated_at = now();
