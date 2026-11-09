-- Japan 1990-94: bubble collapse, then the Emergency Crisis Bailout Package. Paste into Supabase > SQL Editor and run once.
-- Sets a per-year stock change ("yg", % per year, starting 1990) on every Japanese company; after 1994 each company reverts to its normal projected change.
-- Needs the page version that understands "yg". Pages that are open pick it up live (or after a reload).
insert into public.kv (k, v) values
  ('co/NTT', '{"yg":{"1990":-22,"1991":4,"1992":7,"1993":6,"1994":5}}'::jsonb),  -- def
  ('co/Dai-Ichi Kangyo Bank', '{"yg":{"1990":-42,"1991":-8,"1992":6,"1993":9,"1994":8}}'::jsonb),  -- bank
  ('co/Industrial Bank of Japan', '{"yg":{"1990":-42,"1991":-8,"1992":6,"1993":9,"1994":8}}'::jsonb),  -- bank
  ('co/Sumitomo Bank', '{"yg":{"1990":-42,"1991":-8,"1992":6,"1993":9,"1994":8}}'::jsonb),  -- bank
  ('co/Fuji Bank', '{"yg":{"1990":-42,"1991":-8,"1992":6,"1993":9,"1994":8}}'::jsonb),  -- bank
  ('co/Mitsubishi Bank', '{"yg":{"1990":-42,"1991":-8,"1992":6,"1993":9,"1994":8}}'::jsonb),  -- bank
  ('co/Sanwa Bank', '{"yg":{"1990":-42,"1991":-8,"1992":6,"1993":9,"1994":8}}'::jsonb),  -- bank
  ('co/Tokai Bank', '{"yg":{"1990":-42,"1991":-8,"1992":6,"1993":9,"1994":8}}'::jsonb),  -- bank
  ('co/Mitsubishi Trust', '{"yg":{"1990":-42,"1991":-8,"1992":6,"1993":9,"1994":8}}'::jsonb),  -- bank
  ('co/Sumitomo Trust', '{"yg":{"1990":-42,"1991":-8,"1992":6,"1993":9,"1994":8}}'::jsonb),  -- bank
  ('co/Toyota Motor', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Tokyo Electric Power', '{"yg":{"1990":-22,"1991":4,"1992":7,"1993":6,"1994":5}}'::jsonb),  -- def
  ('co/Kansai Electric Power', '{"yg":{"1990":-22,"1991":4,"1992":7,"1993":6,"1994":5}}'::jsonb),  -- def
  ('co/Hitachi', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Matsushita Electric', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Toshiba', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/NEC', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Fujitsu', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Sony', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Nissan Motor', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Honda Motor', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Nippon Steel', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Mitsubishi Heavy Industries', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Nomura Securities', '{"yg":{"1990":-45,"1991":-6,"1992":4,"1993":10,"1994":8}}'::jsonb),  -- sec
  ('co/Daiwa Securities', '{"yg":{"1990":-45,"1991":-6,"1992":4,"1993":10,"1994":8}}'::jsonb),  -- sec
  ('co/Tokio Marine & Fire', '{"yg":{"1990":-30,"1991":-2,"1992":6,"1993":8,"1994":7}}'::jsonb),  -- ins
  ('co/Takeda Chemical', '{"yg":{"1990":-22,"1991":4,"1992":7,"1993":6,"1994":5}}'::jsonb),  -- def
  ('co/Kirin Brewery', '{"yg":{"1990":-22,"1991":4,"1992":7,"1993":6,"1994":5}}'::jsonb),  -- def
  ('co/Arasaka Corporation', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Nintendo', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Sega Enterprises', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Canon', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Nikon', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Fuji Photo Film', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Bridgestone', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Mazda Motor', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Mitsubishi Motors', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Suzuki Motor', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Isuzu Motors', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Yamaha', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Kawasaki Heavy Industries', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Ishikawajima-Harima Heavy Industries', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Mitsubishi Corporation', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Mitsui & Co', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Itochu', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Marubeni', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Sumitomo Corporation', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Mitsubishi Estate', '{"yg":{"1990":-50,"1991":-15,"1992":-5,"1993":4,"1994":6}}'::jsonb),  -- re
  ('co/Mitsui Fudosan', '{"yg":{"1990":-50,"1991":-15,"1992":-5,"1993":4,"1994":6}}'::jsonb),  -- re
  ('co/Japan Air Lines', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/All Nippon Airways', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Ajinomoto', '{"yg":{"1990":-22,"1991":4,"1992":7,"1993":6,"1994":5}}'::jsonb),  -- def
  ('co/Asahi Glass', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Nippon Oil', '{"yg":{"1990":-22,"1991":4,"1992":7,"1993":6,"1994":5}}'::jsonb),  -- def
  ('co/Dai Nippon Printing', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Dentsu', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Nippon Yusen', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Mitsubishi Chemical', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Sumitomo Chemical', '{"yg":{"1990":-33,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb),  -- cyc
  ('co/Sharp', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Sanyo Electric', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Pioneer', '{"yg":{"1990":-28,"1991":14,"1992":16,"1993":10,"1994":6}}'::jsonb),  -- exp
  ('co/Miscellaneous: other Japan listed companies', '{"yg":{"1990":-36,"1991":2,"1992":7,"1993":8,"1994":6}}'::jsonb)  -- misc
on conflict (k) do update set v = coalesce(public.kv.v, '{}'::jsonb) || excluded.v, updated_at = now();
