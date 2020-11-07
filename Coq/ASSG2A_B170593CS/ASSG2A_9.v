Require Import Classical_Prop.
Lemma L1 : forall P Q : Prop, (P \/ Q) <-> ((P -> Q) -> Q).
Proof.
  intros P Q.
  split.
  intro H1.
  case H1.
  intros H2 H3.
  apply H3 in H2.
  exact H2.

  intros H2 H3.
  exact H2.

  intro H1.
  elim (classic Q).
  intro H2.
  right.
  exact H2.

  intro H2.
  elim (classic P).
  intro H3.
  left.
  exact H3.

  intro H3.
  unfold not in H3.
  right.
  apply H1.
  intro H4.
  apply H3 in H4.
  elim H4.
Qed.
Section Prop_Logic_Assg2A.
(* {} |- ((q->p)->p)->((p->q)->q) *)
Variable P Q : Prop.
Lemma ASSG2A_9 : ((Q->P)->P)->((P->Q)->Q).
Proof.
  intro H1.
  intro H2.
  apply L1 in H1.
  case H1.
  intro H3.
  exact H3.
  intro H3.
  apply H2 in H3.
  exact H3.
Qed.