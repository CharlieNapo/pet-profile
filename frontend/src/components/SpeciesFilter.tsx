"use client";

import { useRouter, usePathname, useSearchParams } from "next/navigation";
import styles from "./SpeciesFilter.module.css";

const FILTERS = [
  { value: "all", label: "All" },
  { value: "dog", label: "Dogs" },
  { value: "cat", label: "Cats" },
] as const;

export default function SpeciesFilter() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const currentSpecies = searchParams.get("species") ?? "all";

  function handleFilter(species: string) {
    const params = new URLSearchParams(searchParams.toString());
    if (species === "all") {
      params.delete("species");
    } else {
      params.set("species", species);
    }
    const query = params.toString();
    router.replace(query ? `${pathname}?${query}` : pathname);
  }

  return (
    <div className={styles.filter}>
      {FILTERS.map(({ value, label }) => (
        <button
          key={value}
          onClick={() => handleFilter(value)}
          className={
            currentSpecies === value ? styles.buttonActive : styles.button
          }
        >
          {label}
        </button>
      ))}
    </div>
  );
}
