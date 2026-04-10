import { Suspense } from "react";
import { getPets } from "@/lib/api";
import PetTable from "@/components/PetTable";
import SpeciesFilter from "@/components/SpeciesFilter";
import styles from "./page.module.css";

type Props = {
  searchParams: Promise<{ species?: string }>;
};

export default async function PetListPage({ searchParams }: Props) {
  const { species } = await searchParams;
  const pets = await getPets(species);

  return (
    <div>
      <h1 className={styles.heading}>Pets</h1>
      <Suspense fallback={null}>
        <SpeciesFilter />
      </Suspense>
      <PetTable pets={pets} />
    </div>
  );
}
