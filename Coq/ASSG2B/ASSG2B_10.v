Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable S : V -> (V -> Prop).
  Hypothesis H1 : exists x y : V, S x y \/ S y x.
  Lemma ASSG2B_10 : exists x y : V, S x y.
  Proof.
    destruct H1 as [a H2].
    destruct H2 as [b H2].
    case H2 as [H2_i | H2_ii].
    - exact H2_i.
      - 
